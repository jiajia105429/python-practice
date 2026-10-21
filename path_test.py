from pathlib import Path
p=Path.cwd()
print(p)

p=Path('.')
if p.is_dir():
	new_path=p/"Fishc_txt"
	print(new_path)

for i in p.iterdir():
	if i.is_dir():
		print(i)

for item in p.iterdir():
	if item.is_file():
		print(f"name:{item.name},size:{item.stat().st_size}Byte")
