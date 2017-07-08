INSTRUCTIONS FROM: https://www.dataquest.io/blog/how-to-setup-a-data-science-blog/

STEPS FOR WEB PUBLISHING
1. Navigate to the yazhao.github.io folder
2. Run 'pelican content -s publishconf.py'
3. Run 'git checkout -b dev'
4. Create a commit and push to Github like normal (using git add, git commit, and git push).
5. Run 'ghp-import output -b master' to import everything in the output folder to the master branch.
6. Use 'git push origin master' to push your content to Github.
7. Whenever you make a change to your blog, just re-run the pelican content -s publishconf.py, ghp-import and git push commands above, and your Github Page will be updated.


FOR LOCAL PREVIEW
1. Navigate to the yazhao.github.io folder
2. Run 'pelican content' to generate the HTML.
3. Switch to the output directory.
4. Run 'python -m pelican.server'
5. Visit localhost:8000 in your browser to preview the blog.








