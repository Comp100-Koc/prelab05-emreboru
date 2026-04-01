def longest_palindromic_substring(s):
    max = 0
    palindrome = ""
    
    for i in range(len(s)):
        sol, sağ = i, i
        
        while sol >= 0 and sağ < len(s) and s[sol] == s[sağ]:
            if (sağ - sol + 1)> max:
                max = sağ - sol + 1
                palindrome = s[sol:sağ + 1]
                
            sol -= 1
            sağ += 1
            
        sol, sağ = i, i + 1 
        
        while sol >= 0 and sağ < len(s) and s[sol] == s[sağ]:
            if (sağ-sol + 1 )> max:
                max = sağ-sol + 1 
                palindrome = s[sol:sağ + 1]
                
            sol -= 1
            sağ += 1
            
    if max < 2:
        return ""
    
    return palindrome