# yohaku_APP
「映えないSNS」をコンセプトにしたミニマルなメモ共有アプリ -yohaku-

## users

| カラム名 | 型 | NOT NULL | PK | 備考 |
|----------|----|----------|----|------|
| id | bigint | ○ | ○ | 自動採番 |
| username | varchar(150) | ○ |  | 一意 |
| email | varchar(255) | ○ |  |  |
| created_at | datetime | ○ |  |  |

---

## posts

| カラム名 | 型 | NOT NULL | PK | FK | 備考 |
|----------|----|----------|----|----|------|
| id | bigint | ○ | ○ |  |  |
| user_id | bigint | ○ |  | users.id | 投稿者 |
| content | text | ○ |  |  | 本文 |
| created_at | datetime | ○ |  |  |  |