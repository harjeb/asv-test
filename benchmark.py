class MyBenchmark:
    def setup(self):
        self.mylist = list(range(1000))

    def time_my_function(self):
        my_function(self.mylist)