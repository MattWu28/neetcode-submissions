class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> hashS = new HashMap<>(), hashT = new HashMap<>();
        if (s.length() != t.length()) {
            return false;
        }
        for (int i = 0; i < s.length(); i++) {
            char currS = s.charAt(i), currT = t.charAt(i);
            hashS.put(currS, hashS.getOrDefault(currS, 0) + 1);
            hashT.put(currT, hashT.getOrDefault(currT, 0) + 1);
        }
        return hashS.equals(hashT);
    }
}
