# Beyond 100% test coverage

Code steps for the [Beyond 100% test coverage](https://www.youtube.com/watch?v=AvqtOwWSTcQ&index=20&t=0s&list=PLGN9BI-OAQkRIdWktlyb8ynaapIHTnkVu) talk. Usage:

## Prepare

```bash
$ git config --global alias.demo-start 'checkout demo-start'
$ git config --global alias.demo-next '!git checkout `git rev-list HEAD..demo-end | tail -1`'
$ git config --global alias.demo-prev 'checkout HEAD^'
$ git config --global alias.demo-diff 'diff HEAD^'
$ git config --global alias.demo-msg 'log -1 --pretty=%B'
$ git clone https://github.com/zupo/beyond-100-tests
$ pipenv install
$ pipenv shell
$ export PS1="\$(__git_ps1)\$ "
```

## Talk

Go through commit history. Each commit's diff is one slide, one lesson.  

```bash
$ git demo-start
$ git demo-next
$ git demo-diff
$ git demo-prev
```

### Inspirations and references

* https://blog.jayway.com/2015/03/30/using-git-commits-to-drive-a-live-coding-session/
* https://github.com/niteoweb/Makefile/blob/master/Pipfile
