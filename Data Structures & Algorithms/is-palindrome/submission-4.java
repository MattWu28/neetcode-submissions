class Solution {
    public boolean isPalindrome(String s) {
        int l = 0, r = s.length() - 1;
        while (l < r) {
            char charL = s.charAt(l), charR = s.charAt(r);
            if (!Character.isLetterOrDigit(charL)) {
                l += 1;
                continue;
            }
            if (!Character.isLetterOrDigit(charR)) {
                r -= 1;
                continue;
            }
            if (Character.isDigit(charL)) {
                if (Character.isDigit(charR)) {
                    if (charL == charR) {
                        l += 1;
                        r -= 1;
                        continue;
                    } else {
                        return false;
                    }
                } else {
                    return false;
                }
            } else {
                if (Character.isDigit(charR)) {
                    return false;
                } else {
                    if (Character.toLowerCase(charL) == Character.toLowerCase(charR)) {
                        l += 1;
                        r -= 1;
                        continue;
                    } else {
                        return false;
                    }
                }
            }
        }
        return true;
    }
}