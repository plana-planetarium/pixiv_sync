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

text = text + text_end

with open('.github/workflows/sync.yml', 'w') as sync_write:
    sync_write.write(text)
sync_write.close()

