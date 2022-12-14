import zlib, re, os, base64, json
import requests
from time import time, sleep


# 99% of the code is from sfx2me's hyperion deobf
# The print is from billythegoat356 ( credits to him )
def p(text):
  # sleep(0.05)
  return print(stage(text))
print("Starting")
print("All credit for deobf goes to https://github.com/sfx2me/Hyperion-deobfuscator")
def stage(text: str, symbol: str = '...', col1=light, col2=None) -> str:
  if col2 is None:
    col2 = light if symbol == '...' else purple
  if symbol == '...' or symbol == '!!!':
    return f"""     {Col.Symbol(symbol, col1, dark)} {col2}{text}{Col.reset}"""
  else:
    return f""" {Col.Symbol(symbol, col1, dark)} {col2}{text}{Col.reset}"""

al =requests.get("https://raw.githubusercontent.com/NotAiden030/Microsoft-Gen/main/main.py").content.decode('utf-8')
e = re.findall(r'b64decode\(".*"\)', al)[0].replace('b64decode("', '').replace('")', '')

eo = re.findall(r"https:\/\/pst.klgrth.io\/paste\/\w*\/raw", base64.b64decode(e).decode('utf-8'))[0]

with open("lmaoz.py", "w") as f:
  raq = requests.get(eo).content.decode('utf-8')
  f.write(raq)

System.Size(150, 47)
os.system(
  "clear")

file = "lmaoz.py"
if file == "": file = "in.py"
now = time()
print("\n")
with open(file) as f:
  script = f.read()
try:
  if not "class" in script:
    com = False
    script = script[script.index("b'"):script.rindex("))")]
  else:
    com, ines = True, []
    for l in script.splitlines():
      if r"=b'" in l:
        a = l[l.find("=b'") + len("=b'"):l.rfind("')")]
        ines.append(a)
    script1 = ""
    for l in ines:
      script1 += l
    script = f"b'{script1}'"
  script = zlib.decompress(eval(script)).decode()
except Exception as e:
  sleep(3)
  exit()


lines0 = script.split("\n")

lines = []
lines.clear()
for line in lines0:
  if len(re.sub(r"\s", "", line)) > 0:
    lines.append(line)

try:
  os.remove("temp.py")
  os.remove("out.py")
  os.remove("code.py")
  os.remove("vars.py")
except:
  pass
if com:
  lines = lines[13:]  # first 13 lines are credits
for line in lines:
  with open("temp.py", "a+") as f:
    f.write(line + "\n")


def replace(c, r):
  with open('temp.py', 'r') as file:
    filedata = file.read()
  filedata = filedata.replace(
    c, r
  )  # i must read the file over and over again, because it updates everytime i replace something
  with open('temp.py', 'w') as file:
    file.write(filedata)


def rreplace(c, r):
  with open('out.py', 'r') as file:
    filedata = file.read()
  filedata = filedata.replace(
    c, r
  )  # i must read the file over and over again, because it updates everytime i replace something
  with open('out.py', 'w') as file:
    file.write(filedata)


#x = int(input(stage(f"open temp.py and type the line where the last globals() is (its 15 in 90% of the cases) {dark}-> {Col.reset}", "?", col2 = bpurple)).replace('"','').replace("'",""))
x = 15  # ig its always 15, but not sure
llines = 0

for l in lines:
  llines += 1
  if not ".join" in l:
    if len(l) < 150:
      var = l.split("=", 1)[1]
      code = l[l.find(")") + len(")"):l.rfind("="[0])]
      try:
        decyrpted = eval(code)
      except:
        decyrpted = code
      if "vars" in l:
        code = l[l.find(")") + len(")"):l.rfind("="[0])].replace(
          "[", "").replace("]", "").replace("'", "")
        replace(str(code), "vars")
      decyrpted = str(decyrpted).replace("[", "").replace("]",
                                                          "").replace("'", "")
      replace(str(decyrpted), str(var))

  if llines == x: break
with open("temp.py", "r") as f:
  script = f.read().splitlines()
  lines.clear()
  for line in script:
    lines.append(line)
llines = 0
for l in lines:
  llines += 1
  if not ".join" in l:
    if len(l) > 150:
      var = l.split("=", 1)[1]
      code = l[l.find(")") + len(")"):l.rfind("="[0])].replace(
        "[",
        "").replace("]",
                    "").replace("'",
                                "")  # i could just update the rfind but....
      # print(code)
      #print(var)
      decrypted = eval(var)
      decrypted = str(decrypted)
      if "built-in" in decrypted:
        decrypted = decrypted.replace("<built-in function ", "").replace(
          ">", "")  #im to lazy to get a better way to do this, it works ig
      elif "class" in decrypted:
        decrypted = decrypted.replace("<class '", "").replace("'>", "")
      if "unhexlify" in decrypted:
        decrypted = "binascii.unhexlify"  # we dont talk about this
      replace(str(var), str(decrypted))
      replace(str(code), str(decrypted))
  if llines == x: break
llines = 0
for i in lines:
  llines += 1
  if "from builtins import" in str(i):
    y = int(llines)
    break
with open("temp.py", "r") as f:
  script = f.read().splitlines()
  lines.clear()
  for line in script:
    lines.append(line)

llines = 0
for l in lines:
  llines += 1
  if llines < y and llines > x:
    with open("vars.py", "a+") as f:
      f.write(l + "\n")
  if llines == y: break
llines = 0
for l in lines:
  llines += 1
  if llines >= y:
    #print(l)
    with open("code.py", "a+") as f:
      f.write(l + "\n")
    if llines == len(lines): break

os.system("python3 deobfuscate.py"
          )  # its in a seperate file because its the code from unleqitq

sleep(1)
lines.clear()
if os.path.exists("out.py"):
  with open("out.py", "r") as f:
    script = f.read().splitlines()
    for line in script:
      lines.append(line)
else:
  print("error")
for l in lines:
  if r"binascii.unhexlify" in l and r".decode('8ftu'[::+-+-(-(+1))])" in l:
    code1 = l[l.index(".unhexlify(b'"):l.
              rindex(".decode('8ftu'[::+-+-(-(+1))])")]
    ccode = code1[12:]
    code = eval("__import__('binascii')" + code1 + ".decode('utf8')")
    rreplace(f"eval(binascii{code1}.decode('8ftu'[::+-+-(-(+1))]))", code)

now = round(time() - now, 2)
print('\n')
os.system('clear')

hook = re.findall(r"hook='.*'", open('out.py', 'r').read())[0].replace("hook='", "").replace("'", "")
wh = json.loads(requests.get(hook).content.decode('utf-8'))
print("Webhook retrieved: "+hook)
print(f"Webhook status: {wh.get('message')} [{wh.get('code')}]")
