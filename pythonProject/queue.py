from collections import deque

bank = deque(['ami', 'tumi', 'she'])
print(bank)
bank.popleft()
print(bank)
bank.popleft()
print(bank)
bank.popleft()
if not bank:
    print("no person left")