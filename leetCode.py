nums = int(input("Masukkan angka: "))
num = nums
seen = set()
while nums != 1 and nums not in seen:
    seen.add(nums)
    hasil = 0
    temp = nums
    while temp > 0:
        a = temp % 10  
        hasil += a ** 2 
        temp //= 10  
    nums = hasil
if nums == 1:
    print("Happy Number!")
else:
    print("Unhappy Number!")