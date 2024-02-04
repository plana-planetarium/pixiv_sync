import os

with open('example.yml', 'r') as example_read:
    text = example_read.read()
example_read.close()

name_list = os.listdir('./sync_require/')

text_end = ''

for name in name_list:
    name = name.replace('.txt', '')
    change_part = \
    '\n' + \
    '      - name: Upload File %s\n' % str(name) + \
    '        uses: actions/upload-artifact@v3\n' + \
    '        with:\n' + \
    '          name: %s\n' % str(name) + \
    '          path: ./Downloads/%s/\n' % str(name) + \
    '          if-no-files-found: ignore\n' + \
    '          retention-days: 7\n' + \
    '      - name: Send Email %s\n' % str(name) + \
    '        run: |\n' + \
    '          export NAME_USER="%s"\n' % str(name) + \
    '          python upload_email.py\n\n'
    text_end += change_part

text_git = \
    '      - name: Git push log\n' + \
    '        run: |\n' + \
    '          mkdir ../push_resp\n' + \
    '          mkdir ../push_resp/downloads_log\n' + \
    '          mv ./downloads_log/* ../push_resp/downloads_log/\n' + \
    '          cd ../push_resp\n' + \
    '          git clone https://github.com/plana-planetarium/pixiv_sync.git\n' + \
    '          git config --global user.name "plana-planetarium"\n' + \
    '          git config --global user.email "3412294524@qq.com"\n' + \
    '          cd pixiv_sync\n' + \
    '          rm -rf downloads_log\n' + \
    '          mkdir downloads_log\n' + \
    '          mv ../downloads_log/* ./downloads_log/\n' + \
    '          rm -rf /home/runner/work/pixiv_sync/push_resp/pixiv_sync/.git/\n' + \
    '          git init\n' + \
    '          git remote add origin git@github.com:plana-planetarium/pixiv_sync.git\n' + \
    '          git add ./downloads_log\n' + \
    '          git commit -m "Update downloads logs"\n\n' + \
    '      - name: Push\n' + \
    '        uses: ad-m/github-push-action@master\n' + \
    '        with:\n' + \
    '          github_token: ${{ secrets.TOKEN }}\n'

text = text + text_end + text_git

with open('.github/workflows/sync.yml', 'w') as sync_write:
    sync_write.write(text)
sync_write.close()

