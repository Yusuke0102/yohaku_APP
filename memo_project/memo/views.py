# views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .forms import MemoForm
from .models import Memo, Like
from django.http import Http404
from django.db import IntegrityError, transaction
from django.db.models import OuterRef, F
from django.db.models.expressions import Exists
from django.views.decorators.http import require_http_methods, require_POST
from django.views.decorators.cache import never_cache

@never_cache
@login_required
def memo(request):
    qs = Memo.objects.all().order_by('-created_at')
    
    like = Like.objects.filter(
        user=request.user,
        memo=OuterRef('pk')
    )
    
    memos = qs.annotate(
        is_liked=Exists(like)
    )

    return render(request, "memo/memo.html", {
        "memos": memos,
    })

@never_cache
@login_required
@require_http_methods(["GET", "POST"])
def create_memo(request):
    form = MemoForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        memo = form.save(commit=False)
        memo.user = request.user
        memo.save() 
        return redirect("memo")

    return render(request, "memo/create_memo.html", {
            "form": form
    })

@never_cache
@require_http_methods(["GET", "POST"])
@login_required
def delete_memo(request, memo_id):
    memo = Memo.objects.get(id=memo_id, user=request.user)
    if request.method == "POST":
        memo.delete()
        return redirect("memo")

    return render(request, "memo/delete_memo.html", {
        "memo": memo
    })     

@never_cache
@require_http_methods(["GET", "POST"])
@login_required
def edit_memo(request, memo_id):
    memo = Memo.objects.get(id=memo_id, user=request.user)
    form = MemoForm(request.POST or None, instance=memo)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("memo")
        else:
            return render(request, "memo/edit_memo.html", {
                "form": form,
                "memo": memo,
                "IsError": "True"
            })

    return render(request, "memo/edit_memo.html", {
        "form": form,
        "memo": memo
    })

@never_cache
@require_POST
@login_required
def like_memo(request, memo_id):
    try:
        memo =Memo.objects.get(id=memo_id)
    except Memo.DoesNotExist:
        raise Http404()
    
    with transaction.atomic():
        deleted, _ = Like.objects.filter(user=request.user, memo=memo).delete()

        if deleted:
            Memo.objects.filter(id=memo_id).update(likescount=F("likescount") - 1)
            state = "unliked"
        else:
            Like.objects.create(user=request.user, memo=memo)
            Memo.objects.filter(id=memo_id).update(likescount=F("likescount") + 1)
            state = "liked"

        memo.refresh_from_db(fields=["likescount"])
        return render(request, "memo/like_memo.html", {
            "memo": memo,
            "state": state
        })