def maximize_earning(earnings, k):
    n = len(earnings)
    if n == 0:
        return 0
    # Precompute prefix sums to quickly calculate the sum of any subarray
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + earnings[i]
    
    dp = [0] * n  # dp[i] represents the maximum earnings ending at day i
    
    for i in range(n):
        current_max = 0
        for m in range(1, k + 1):
            start = i - m + 1
            if start < 0:
                continue  # Not enough days to form m-length subarray
            # Calculate sum of subarray from start to i inclusive
            sum_m = prefix_sum[i + 1] - prefix_sum[start]
            # Previous index is i - m - 1 (the day before the start of the current subarray minus one)
            prev_i = i - m - 1
            prev = dp[prev_i] if prev_i >= 0 else 0
            current = sum_m + prev
            if current > current_max:
                current_max = current
        dp[i] = current_max
    
    return max(dp) if dp else 0
    


print(maximize_earning([60, 70, 80, 40, 80, 90, 100, 20], 3))
print(maximize_earning([45, 12, 78, 34, 56, 89, 23, 67, 91],4))

# 8 / 3= 6 rem 2
# Now I'm supposed to divide 6 / rest days = 3
