Instructions taken from: https://www.dataquest.io/blog/how-to-setup-a-data-science-blog/

## Steps for Web Publishing
1. Navigate to the yazhao.github.io folder
2. Run 'pelican content -s publishconf.py'
3. Create a commit and push to Github like normal (using git add, git commit, and git push).
4. Run 'ghp-import output -b master' to import everything in the output folder to the master branch.
5. Use 'git push origin master' to push your content to Github.
6. Whenever you make a change to your blog, just re-run the pelican content -s publishconf.py, ghp-import and git push commands above, and your Github Page will be updated.

## For Local Preview
1. Navigate to the yazhao.github.io folder
2. Run 'pelican content' to generate the HTML.
3. Switch to the output directory.
4. Run 'python -m pelican.server'
5. Visit localhost:8000 in your browser to preview the blog.








