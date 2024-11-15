apply_patch:
	# https://stackoverflow.com/questions/70503219/python-selenium-webdrive-cannot-upload-file-with-unknown-command-exception
	sed -i -e 's/se\/file/file/g' $(shell python -c 'import sysconfig; print(sysconfig.get_paths()["purelib"])')/selenium/webdriver/remote/remote_connection.py

#Запустить линтеры. Flake8 - напишет в консоль ошибки по коду. Black - автоматически поправит форматирование.
run_linter:
	flake8
	black .