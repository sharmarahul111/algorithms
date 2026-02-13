# Primes
Computing and analyzing first N prime numbers
Current status: 20M in ~10 minutes (in C)
Update: 41M in ~ minute with sieve method
## Optimizations
- mod only by previous primes (not every number) 🚀
- stop at √n for if n is prime 🚀
- increment mod operand by 2 (evens don't matter) 🐢
- don't mod by 2 🐢

- sieve method 🚀🚀🚀
## TODO:
- A program which starts where it left computing primes
- efficient storage of the primes (in binary)
- better charts
  - analyze the data of primes in various graphs
  - logs, diffs, number of primes, etc
  - try to see the nature of primes
- compute upto 100M primes somehow
