# Звіт з лабораторної роботи 02

**ПІБ:** Мазурик Матвій Сергійович
**Група:** ІПЗ-22
**Роль у команді:** Dev
**Репозиторій:** https://github.com/IceStormSS/lab02-git

## Особистий внесок

**Гілки:**
- `feature/convertor`
- `docs/report-a`

**Pull Request:**
- #1 feat: add converter module —  https://github.com/IceStormSS/lab02-git/pull/2
- #? docs: update project description (A) — https://github.com/IceStormSS/lab02-git/pull/3
- #? docs: update README — https://github.com/IceStormSS/lab02-git/pull/5

**Коміти:**
- feat: add calculator module — https://github.com/IceStormSS/lab02-git/pull/1/commits
- docs: update project description (A) — https://github.com/IceStormSS/lab02-git/pull/5
- docs: update README — https://github.com/IceStormSS/lab02-git/pull/5/commits

**Ревʼю:** перевірив Pull Request товариша (feature/converter, docs/changelog), залишив коментарі та схвалив зміни.

## Вирішений конфлікт

Конфлікт виник у файлі `README.md`: у гілці `feature/readme-a` я змінив другий рядок, а мій товариш у гілці `feature/readme-b` змінив той самий рядок по-іншому. Після злиття моєї гілки в `main` його Pull Request показав конфлікт. Він вирішив його локально командами `git fetch origin` та `git merge origin/main`, вручну обрав потрібний варіант тексту, видалив маркери `<<<<<<<`, `=======`, `>>>>>>>` і зробив коміт.

![конфлікт]: https://ibb.co/HfgHv06F

## Висновки

У ході роботи я налаштував Git, SSH-доступ і двофакторну автентифікацію на GitHub, навчився працювати з гілками та Pull Request-ами. Я побачив, як виникає конфлікт злиття і як його вирішувати, а також як проходить code review в команді.