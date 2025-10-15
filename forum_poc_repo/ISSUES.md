
# GitHub Issues (Detailed PoC) — Tasks with estimates

## Epic: Project setup (2d)
- [ ] Initialize repository, add CONTRIBUTING.md and CODE_OF_CONDUCT.md. (2h)
- [ ] Setup CI (GitHub Actions) with lint + basic job. (4h)
- [ ] Create Makefile and start scripts for local dev. (2h)

## Epic: Backend MVP (5d)
- [ ] Django project scaffolding and shops app. (4h)
- [ ] Models: Shop, ShopCategory, Review, PromotionPlan, Payment. (1d)
- [ ] Serializers & ViewSets for Shop + tests. (1d)
- [ ] Auth: registration, login, email verification (using Django auth + simple token). (1d)
- [ ] Admin: register models in admin. (4h)
- [ ] Background tasks: configure Celery + Redis (skeleton). (4h)

## Epic: Frontend MVP (5d)
- [ ] Next.js app skeleton and routes. (4h)
- [ ] Shop listing page (fetch /api/shops) with SSR. (1d)
- [ ] Shop detail page with structured data (schema.org). (1d)
- [ ] Auth flow (login/register) and integration with backend. (1d)
- [ ] Simple UI kit (buttons, cards, forms). (8h)

## Epic: Core features (7d)
- [ ] Search & filters (Postgres full-text indexing for MVP). (2d)
- [ ] Reviews & ratings (backend + frontend). (2d)
- [ ] Promotion plans & payments (Stripe integration - skeleton). (2d)
- [ ] User dashboard (seller) — view/manage shops, stats. (1d)
- [ ] Moderation tools: reports, approve/reject shops/reviews. (1d)

## Epic: Ops & Security (3d)
- [ ] HTTPS/SSL, secrets management and env docs. (4h)
- [ ] Monitoring: Sentry + basic Prometheus metrics. (1d)
- [ ] Backups & migrations strategy (db dumps + retention). (1d)

## Epic: Tests & QA (2d)
- [ ] Unit tests for backend endpoints (shops). (1d)
- [ ] e2e tests for critical flows (signup, create shop, view shop). (1d)

---
Notes:
- Estimates are rough and assume one mid-level developer.
- Break down large tasks into subtasks when creating GitHub Issues.
