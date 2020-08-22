# fastapi-sentiment
![copilot-image](https://images.unsplash.com/photo-1494367079857-303d616995e9?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=825&q=80)
A FastAPI sentiment analysis API deployed onto Amazon ECS via `copilot` to serve sentiment analysis predictions.

Prefer words over code? Check out the blog post [here](https://lifewithdata.org/aws-ecs-copilot-cli).

## Quick Start
```bash
make build test
copilot init
copilot env init --name prod --profile default --app fastapi-sentiment
copilot svc deploy --name fastapi-sentiment --env prod
```
