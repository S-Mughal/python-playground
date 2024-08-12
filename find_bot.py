def find_bot(log: str, count: int) -> list[str]:
  ip = []
  bots = []
  [ip.append(i.split(",")[1] for i in log]
  ip_set = set(ip)
  for i in ip_set:
    if ip.count(i) >= count:
      bots.append(i)
  print(bots)

logs = [
  "1722024582, 52.0.1.1",
  "1722024582, 52.0.1.1",
  "1722024582, 52.0.1.1",
  "1722024582, 52.0.1.1",
]
