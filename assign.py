import re

file = open('regex_sum_166846.txt')
jml = 0
for line in file:
	line_strip = line.rstrip()
	num = re.findall('[0-9]+', line_strip)
	if len(num) > 0:
		for n in num:
			angka = int(n)
			jml = jml + angka
print(jml)
