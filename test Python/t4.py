# a = 'This is a test string from Andrew 1 2 3 4 5 6 7 8 9 0'
# print(sorted(a.split(), key=lambda x: x.upper()))

class MyIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.end:
            result = self.current
            self.current += 1
            return result
        else:
            raise StopIteration

# สร้าง Iterator
my_iterator = MyIterator(1, 5)

# ใช้ Iterator ในการวนลูป
for number in my_iterator:
    print(number)
