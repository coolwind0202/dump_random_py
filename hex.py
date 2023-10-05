import random

def hex_padding(n: int, width: int = 2):
  # 整数を16進数にしパディングする
  return hex(n)[2:].zfill(width)

def blue_str(s: str):
  # 文字列を青色で表示する
  return f"\033[34m{s}\033[37m"

def header():
  return " " * 5 + "\t| " + blue_str(" ".join([hex_padding(i) for i in range(16)]))

def print_hexstr(s: str):
  l: list[bytes] = []

  # 2文字ずつ取り出して1バイトの bytes に変換
  for i in range(0, len(s), 2):
    l.append(bytes.fromhex(s[i: i+2]))

  # ヘッダーを表示
  print(header())

  for i, byte in enumerate(l):
    if i % 16 == 0:
      if i:
        # 2行目以降に到達したら、改行する
        print()
      # 表示中のバイト数を16進数で表示する
      print(blue_str(hex_padding(i, 5)), end = "\t| ")
    print(byte.hex(), end = " ")
  print()

def get_hexstr(byte_count: int) -> str:
  # バイト数 byte_count の16進数文字列を生成
  return "".join([hex_padding(random.randint(0x00, 0xff)) for _ in range(byte_count)])

def main():
  s = get_hexstr(100)
  print(s)
  print_hexstr(s)

if __name__ == "__main__":
  main()