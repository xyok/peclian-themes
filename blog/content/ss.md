Title: ss
Date: 2010-12-03 10:20
Category: note
Tags: git
Authors: xyok

---
title: git_note
date: 2016-09-07 18:53:14
tags: 
- git 
- tutorial
---

# git note

## 0. usage

```
usage: git [--version] [--help] [-C <path>] [-c name=value]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | --no-pager] [--no-replace-objects] [--bare]
           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
           <command> [<args>]

这些是各种场合常见的 Git 命令：

开始一个工作区（参见：git help tutorial）
   clone      克隆一个仓库到一个新目录
   init       创建一个空的 Git 仓库或重新初始化一个已存在的仓库

在当前变更上工作（参见：git help everyday）
   add        添加文件内容至索引
   mv         移动或重命名一个文件、目录或符号链接
   reset      重置当前 HEAD 到指定状态
   rm         从工作区和索引中删除文件

检查历史和状态（参见：git help revisions）
   bisect     通过二分查找定位引入 bug 的提交
   grep       输出和模式匹配的行
   log        显示提交日志
   show       显示各种类型的对象
   status     显示工作区状态

扩展、标记和调校您的历史记录
   branch     列出、创建或删除分支
   checkout   切换分支或恢复工作区文件
   commit     记录变更到仓库
   diff       显示提交之间、提交和工作区之间等的差异
   merge      合并两个或更多开发历史
   rebase     本地提交转移至更新后的上游分支中
   tag        创建、列出、删除或校验一个 GPG 签名的标签对象

协同（参见：git help workflows）
   fetch      从另外一个仓库下载对象和引用
   pull       获取并整合另外的仓库或一个本地分支
   push       更新远程引用和相关的对象

命令 'git help -a' 和 'git help -g' 显示可用的子命令和一些概念帮助。
查看 'git help <命令>' 或 'git help <概念>' 以获取给定子命令或概念的
帮助。

```

##  1. 初始化

```
用法：git init [-q | --quiet] [--bare] [--template=<模板目录>] [--shared[=<权限>]] [<目录>]

    --template <模板目录>
                          模板目录将被使用
    --bare                创建一个纯仓库
    --shared[=<权限>]     指定 git 仓库是多个用户之间共享的
    -q, --quiet           静默模式
    --separate-git-dir <git目录>
                          git目录和工作区分离

```

## 2. 克隆

```
用法：git clone [<选项>] [--] <仓库> [<路径>]

    -v, --verbose         更加详细
    -q, --quiet           更加安静
    --progress            强制显示进度报告
    -n, --no-checkout     不创建一个检出
    --bare                创建一个纯仓库
    --mirror              创建一个镜像仓库（也是纯仓库）
    -l, --local           从本地仓库克隆
    --no-hardlinks        不使用本地硬链接，始终复制
    -s, --shared          设置为共享仓库
    --recursive           在克隆时初始化子模组
    --recurse-submodules  在克隆时初始化子模组
    --template <模板目录>
                          模板目录将被使用
    --reference <仓库>    参考仓库
    --dissociate          仅在克隆时参考 --reference 指向的本地仓库
    -o, --origin <名称>   使用 <名称> 而不是 'origin' 去跟踪上游
    -b, --branch <分支>   检出 <分支> 而不是远程 HEAD
    -u, --upload-pack <路径>
                          远程 git-upload-pack 路径
    --depth <深度>        创建一个指定深度的浅克隆
    --single-branch       只克隆一个分支、HEAD 或 --branch
    --separate-git-dir <git目录>
                          git目录和工作区分离
    -c, --config <key=value>
                          在新仓库中设置配置信息


```

## 3. git add

```
用法：git add [<选项>] [--] <路径规格>...

    -n, --dry-run         演习
    -v, --verbose         冗长输出

    -i, --interactive     交互式拣选
    -p, --patch           交互式挑选数据块
    -e, --edit            编辑当前差异并应用
    -f, --force           允许添加忽略的文件
    -u, --update          更新已跟踪的文件
    -N, --intent-to-add   只记录，该路径稍后再添加
    -A, --all             添加所有改变的已跟踪文件和未跟踪文件
    --ignore-removal      忽略工作区中移除的路径（和 --no-all 相同）
    --refresh             不添加，只刷新索引
    --ignore-errors       跳过因出错不能添加的文件
    --ignore-missing      检查在演习模式下文件（即使不存在）是否被忽略

```

## 4. git log

```
用法：git log [<选项>] [<版本范围>] [[--] <路径>...]
   或：git show [<选项>] <对象>...

    -q, --quiet           不显示差异输出
    --source              显示源
    --use-mailmap         使用邮件映射文件
    --decorate[=...]      修饰选项
    -L <n,m:file>         处理文件中第 n 到 m 之间的行，从 1 开始

```

## 5. git status

```
用法：git status [<选项>] [--] <路径规格>...

    -v, --verbose         冗长输出
    -s, --short           以简洁的格式显示状态
    -b, --branch          显示分支信息
    --porcelain           机器可读的输出
    --long                以长格式显示状态（默认）
    -z, --null            条目以 NUL 字符结尾
    -u, --untracked-files[=<模式>]
                          显示未跟踪的文件，“模式”的可选参数：all、normal、no。（默认：all）
    --ignored             显示忽略的文件
    --ignore-submodules[=<何时>]
                          忽略子模组的更改，“何时”的可选参数：all、dirty、untracked。（默认：all）
    --column[=<风格>]     以列的方式显示未跟踪的文件

```

## 6. 分支

```
用法：git branch [<选项>] [-r | -a] [--merged | --no-merged]
   或：git branch [<选项>] [-l] [-f] <分支名> [<起始点>]
   或：git branch [<选项>] [-r] (-d | -D) <分支名>...
   或：git branch [<选项>] (-m | -M) [<旧分支>] <新分支>
   或：git branch [<选项>] [-r | -a] [--points-at]

通用选项
    -v, --verbose         显示哈希值和主题，若参数出现两次则显示上游分支
    -q, --quiet           不显示信息
    -t, --track           设置跟踪模式（参见 git-pull(1)）
    --set-upstream        改变上游信息
    -u, --set-upstream-to <upstream>
                          change the upstream info
    --unset-upstream      Unset the upstream info
    --color[=<何时>]      使用彩色输出
    -r, --remotes         作用于远程跟踪分支
    --contains <提交>     只打印包含该提交的分支
    --abbrev[=<n>]        用 <n> 位数字显示 SHA-1 哈希值

具体的 git-branch 动作：
    -a, --all             列出远程跟踪及本地分支
    -d, --delete          删除完全合并的分支
    -D                    删除分支（即使没有合并）
    -m, --move            移动/重命名一个分支，以及它的引用日志
    -M                    移动/重命名一个分支，即使目标已存在
    --list                列出分支名
    -l, --create-reflog   创建分支的引用日志
    --edit-description    标记分支的描述
    -f, --force           强制创建、移动/重命名、删除
    --merged <提交>       只打印已经合并的分支
    --no-merged <提交>    只打印尚未合并的分支
    --column[=<风格>]     以列的方式显示分支
    --sort <key>          排序的字段名
    --points-at <对象>    只打印指向该对象的分支

```

## 7. git checkout

```
用法：git checkout [<选项>] <分支>
   或：git checkout [<选项>] [<分支>] -- <文件>...

    -q, --quiet           不显示进度报告
    -b <分支>             创建并检出一个新的分支
    -B <分支>             创建/重置并检出一个分支
    -l                    为新的分支创建引用日志
    --detach              成为指向该提交的分离头指针
    -t, --track           为新的分支设置上游信息
    --orphan <新分支>     新的没有父提交的分支
    -2, --ours            对尚未合并的文件检出我们的版本
    -3, --theirs          对尚未合并的文件检出他们的版本
    -f, --force           强制检出（丢弃本地修改）
    -m, --merge           和新的分支执行三方合并
    --overwrite-ignore    更新忽略的文件（默认）
    --conflict <风格>     冲突输出风格（merge 或 diff3）
    -p, --patch           交互式挑选数据块
    --ignore-skip-worktree-bits
                          对路径不做稀疏检出的限制
    --ignore-other-worktrees
                          不检查指定的引用是否被其他工作区所占用
    --progress            强制显示进度报告

```

## 8. git commit

```
用法：git commit [<选项>] [--] <路径规格>...

    -q, --quiet           提交成功后不显示概述信息
    -v, --verbose         在提交说明模板里显示差异

提交说明选项
    -F, --file <文件>     从文件中读取提交说明
    --author <作者>       提交时覆盖作者
    --date <日期>         提交时覆盖日期
    -m, --message <说明>  提交说明
    -c, --reedit-message <提交>
                          重用并编辑指定提交的提交说明
    -C, --reuse-message <提交>
                          重用指定提交的提交说明
    --fixup <提交>        使用 autosquash 格式的提交说明用以修正指定的提交
    --squash <提交>       使用 autosquash 格式的提交说明用以压缩至指定的提交
    --reset-author        现在将该提交的作者改为我（和 -C/-c/--amend 参数共用）
    -s, --signoff         添加 Signed-off-by: 签名
    -t, --template <文件>
                          使用指定的模板文件
    -e, --edit            强制编辑提交
    --cleanup <default>   设置如何删除提交说明里的空格和#注释
    --status              在提交说明模板里包含状态信息
    -S, --gpg-sign[=<key-id>]
                          GPG 提交签名

提交内容选项
    -a, --all             提交所有改动的文件
    -i, --include         添加指定的文件到索引区等待提交
    --interactive         交互式添加文件
    -p, --patch           交互式添加变更
    -o, --only            只提交指定的文件
    -n, --no-verify       绕过 pre-commit 钩子
    --dry-run             显示将要提交的内容
    --short               以简洁的格式显示状态
    --branch              显示分支信息
    --porcelain           机器可读的输出
    --long                以长格式显示状态（默认）
    -z, --null            条目以 NUL 字符结尾
    --amend               修改先前的提交
    --no-post-rewrite     绕过 post-rewrite 钩子
    -u, --untracked-files[=<模式>]
                          显示未跟踪的文件，“模式”的可选参数：all、normal、no。（默认：all）

```

## 9. 合并

```
用法：git merge [<选项>] [<提交>...]
   或：git merge [<选项>] <说明> HEAD <提交>
   或：git merge --abort

    -n                    在合并的最后不显示差异统计
    --stat                在合并的最后显示差异统计
    --summary             （和 --stat 同义）
    --log[=<n>]           在合并提交信息中添加（最多 <n> 条）精简提交记录
    --squash              创建一个单独的提交而不是做一次合并
    --commit              如果合并成功，执行一次提交（默认）
    -e, --edit            在提交前编辑提交说明
    --ff                  允许快进（默认）
    --ff-only             如果不能快进就放弃合并
    --rerere-autoupdate   如果可能，重用冲突解决更新索引
    --verify-signatures   验证指定的提交是否包含一个有效的 GPG 签名
    -s, --strategy <策略>
                          要使用的合并策略
    -X, --strategy-option <option=value>
                          所选的合并策略的选项
    -m, --message <说明>  合并的提交说明（针对非快进式合并）
    -v, --verbose         更加详细
    -q, --quiet           更加安静
    --abort               放弃当前正在进行的合并
    --progress            强制显示进度报告
    -S, --gpg-sign[=<key-id>]
                          GPG 提交签名
    --overwrite-ignore    更新忽略的文件（默认）


```


## 10. 标签

```
用法：git tag [-a | -s | -u <key-id>] [-f] [-m <说明> | -F <文件>] <标签名> [<头>]
   或：git tag -d <标签名>...
   或：git tag -l [-n[<数字>]] [--contains <提交>] [--points-at <对象>]
		[--format=<格式>] [--[no-]merged [<提交>]] [<模式>...]
   或：git tag -v <标签名>...

    -l, --list            列出标签名称
    -n[<n>]               每个标签信息打印 <n> 行
    -d, --delete          删除标签
    -v, --verify          验证标签

标签创建选项
    -a, --annotate        附注标签，需要一个说明
    -m, --message <说明>  标签说明
    -F, --file <文件>     从文件中读取提交说明
    -s, --sign            附注并附加 GPG 签名的标签
    --cleanup <模式>      设置如何删除提交说明里的空格和#注释
    -u, --local-user <key-id>
                          使用另外的私钥签名该标签
    -f, --force           如果存在，替换现有的标签
    --create-reflog       创建引用日志

标签列表选项
    --column[=<风格>]     以列的方式显示标签列表
    --contains <提交>     只打印包含提交的标签
    --merged <提交>       只打印已经合并的标签
    --no-merged <提交>    只打印尚未合并的标签
    --sort <key>          排序的字段名
    --points-at <对象>    只打印对象的标签
    --format <格式>       输出格式

```

## 11. 协同

```
用法：git fetch [<选项>] [<仓库> [<引用规格>...]]
   或：git fetch [<选项>] <组>
   或：git fetch --multiple [<选项>] [(<仓库> | <组>)...]
   或：git fetch --all [<选项>]

    -v, --verbose         更加详细
    -q, --quiet           更加安静
    --all                 从所有的远程抓取
    -a, --append          追加到 .git/FETCH_HEAD 而不是覆盖它
    --upload-pack <路径>  上传包到远程的路径
    -f, --force           强制覆盖本地分支
    -m, --multiple        从多个远程抓取
    -t, --tags            抓取所有的标签和关联对象
    -n                    不抓取任何标签(--no-tags)
    -p, --prune           清除远程已经不存在的分支的跟踪分支
    --recurse-submodules[=<on-demand>]
                          控制子模组的递归抓取
    --dry-run             演习
    -k, --keep            保持下载包
    -u, --update-head-ok  允许更新 HEAD 引用
    --progress            强制显示进度报告
    --depth <深度>        深化浅克隆的历史
    --unshallow           转换为一个完整的仓库
    --update-shallow      接受更新 .git/shallow 的引用
    --refmap <引用映射>   指定获取操作的引用映射

```


```
用法：git pull [<选项>] [<仓库> [<引用规格>...]]

    -v, --verbose         更加详细
    -q, --quiet           更加安静
    --progress            强制显示进度报告

和合并相关的选项
    -r, --rebase[=<false|true|preserve>]
                          使用变基操作取代合并操作以合入修改
    -n                    在合并的最后不显示差异统计
    --stat                在合并的最后显示差异统计
    --log[=<n>]           在合并提交信息中添加（最多 <n> 条）精简提交记录
    --squash              创建一个单独的提交而不是做一次合并
    --commit              如果合并成功，执行一次提交（默认）
    --edit                在提交前编辑提交说明
    --ff                  允许快进式
    --ff-only             如果不能快进就放弃合并
    --verify-signatures   验证指定的提交是否包含一个有效的 GPG 签名
    -s, --strategy <策略>
                          要使用的合并策略
    -X, --strategy-option <option=value>
                          所选的合并策略的选项
    -S, --gpg-sign[=<key-id>]
                          GPG 提交签名

和获取相关的参数
    --all                 从所有的远程抓取
    -a, --append          追加到 .git/FETCH_HEAD 而不是覆盖它
    --upload-pack <路径>  上传包到远程的路径
    -f, --force           强制覆盖本地分支
    -t, --tags            抓取所有的标签和关联对象
    -p, --prune           清除远程已经不存在的分支的跟踪分支
    --recurse-submodules[=<on-demand>]
                          控制子模组的递归抓取
    --dry-run             演习
    -k, --keep            保持下载包
    --depth <深度>        深化浅克隆的历史
    --unshallow           转换为一个完整的仓库
    --update-shallow      接受更新 .git/shallow 的引用
    --refmap <引用映射>   指定获取操作的引用映射

```


```
用法：git push [<选项>] [<仓库> [<引用规格>...]]

    -v, --verbose         更加详细
    -q, --quiet           更加安静
    --repo <仓库>         仓库
    --all                 推送所有引用
    --mirror              镜像所有引用
    --delete              删除引用
    --tags                推送标签（不能使用 --all or --mirror）
    -n, --dry-run         演习
    --porcelain           机器可读的输出
    -f, --force           强制更新
    --force-with-lease[=<引用名>:<期望值>]
                          要求引用旧的取值为设定值
    --recurse-submodules[=<check|on-demand|no>]
                          控制子模组的递归推送
    --thin                使用精简打包
    --receive-pack <receive-pack>
                          接收包程序
    --exec <receive-pack>
                          接收包程序
    -u, --set-upstream    设置 git pull/status 的上游
    --progress            强制显示进度报告
    --prune               清除本地删除的引用
    --no-verify           绕过 pre-push 钩子
    --follow-tags         推送缺失但有关的标签
    --signed[=<yes|no|if-asked>]
                          用 GPG 为推送签名
    --atomic              需要远端支持原子事务

```


## 12. 远端

```
用法：git remote [-v | --verbose]
   或：git remote add [-t <分支>] [-m <master>] [-f] [--tags | --no-tags] [--mirror=<fetch|push>] <名称> <地址>
   或：git remote rename <旧名称> <新名称>
   或：git remote remove <名称>
   或：git remote set-head <名称> (-a | --auto | -d | --delete | <分支>)
   或：git remote [-v | --verbose] show [-n] <名称>
   或：git remote prune [-n | --dry-run] <名称>
   或：git remote [-v | --verbose] update [-p | --prune] [(<组> | <远程>)...]
   或：git remote set-branches [--add] <名称> <分支>...
   或：git remote get-url [--push] [--all] <名称>
   或：git remote set-url [--push] <名称> <新的地址> [<旧的地址>]
   或：git remote set-url --add <名称> <新的地址>
   或：git remote set-url --delete <名称> <地址>

    -v, --verbose         冗长输出；必须置于子命令之前

```





