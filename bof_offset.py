import pwn



for offset in range(1,10000):
	p = pwn.process('./babyrop_level1_testing1')
	p.sendline('a'*offset)
	t = p.recvall()
	print(t)
	return_code = p.poll(True)
	if return_code == -11 :
		print('[*] you found offset')
		offset = offset -1
		break

if offset== 10000:
	print("[!] Couldn't find offset")
	exit()

print(f'[+] Your offset is: {offset}')
