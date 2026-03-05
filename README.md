# sample_codespace_project

[参考](https://zenn.dev/yuiseki/articles/89b62b1cfdfaf0)

## Setup

1. Open in GitHub Codespace.
2. Run `docker compose up -d` in the terminal to start PostgreSQL and the app container.  
   ⚠️ **If you see an error like**
   ```
   unable to get image 'postgres:14': Error response from daemon: client version 1.53 is too new. Maximum supported API version is 1.43
   ```
   it means the Docker CLI inside the devcontainer is newer than the host daemon.  
   The devcontainer now sets `DOCKER_API_VERSION=1.43`, or you can downgrade/upgrade Docker so both sides match.
3. Run `docker compose exec app python app.py` to test the PostgreSQL connection.

PostgreSQL is available on port 5432 with database 'mydb', user 'user', password 'password'.