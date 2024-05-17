#!/usr/bin/python3

def isWinner(x, nums):
    """
    Determines the winner of the prime game.

    Args:
        x (int): The number of rounds to be played.
        nums (List[int]): A list of integers representing the number of
        stones in each round.

    Returns:
        str or None: The name of the winner (either "Maria" or "Ben")
        or None if there is no winner.

    """

    def sieve_of_eratosthenes(limit):
        """
        Generate a list of prime numbers up to the given limit using the
        Sieve of Eratosthenes algorithm.

        Args:
            limit (int): The upper limit for generating prime numbers.

        Returns:
            list: A list of prime numbers up to the given limit.
        """
        sieve = [True] * (limit + 1)
        sieve[0] = sieve[1] = False
        for num in range(2, int(limit**0.5) + 1):
            if sieve[num]:
                for multiple in range(num * num, limit + 1, num):
                    sieve[multiple] = False
        return [num for num, is_prime in enumerate(sieve) if is_prime]

    def play_game(n):
        """
        Play the prime game.

        Args:
            n (int): The number to play the game with.

        Returns:
            int: The player who wins the game (0 for Maria, 1 for Ben).
        """
        primes = sieve_of_eratosthenes(n)
        # Initialize the player who starts first
        current_player = 0  # 0 for Maria, 1 for Ben
        while n > 1:
            # Find the largest prime number less than or equal to n
            for prime in reversed(primes):
                if prime <= n:
                    n -= prime
                    current_player = 1 - current_player  # Switch players
                    break
        return current_player

    maria_wins = ben_wins = 0
    for n in nums:
        winner = play_game(n)
        if winner == 0:
            maria_wins += 1
        elif winner == 1:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
