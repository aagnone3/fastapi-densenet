# fastapi-mobilenet
FastAPI deployed onto Amazon ECS via `copilot` to serve sentiment analysis predictions.

Prefer words over code? Check out the blog post [here](https://lifewithdata.org/aws-ecs-copilot-cli).

## Quick Start
```bash
make build test
copilot init
copilot env init --name prod --profile default --app fastapi-sentiment
copilot svc deploy --name fastapi-sentiment --env prod
```
