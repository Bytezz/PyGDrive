pre=/usr/local/bin/

install:
	mkdir -p $(pre)
	cp pygdrive $(pre)pygdrive
	cp client_secrets.json $(pre)client_secrets.json
	chmod +x $(pre)pygdrive
	chmod +x $(pre)client_secrets.json

uninstall:
	rm $(pre)pygdrive
	rm $(pre)client_secrets.json

reinstall:
	rm $(pre)pygdrive
	rm $(pre)client_secrets.json
	cp pygdrive $(pre)pygdrive
	cp client_secrets.json $(pre)client_secrets.json
	chmod +x $(pre)pygdrive
	chmod +x $(pre)client_secrets.json
