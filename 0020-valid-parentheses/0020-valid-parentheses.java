class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        Set<Character> opens = Set.of('(', '{', '[');
        for(int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (opens.contains(c)) {
                stack.push(c);
            } else {
                if(stack.isEmpty()) return false;

                char top = stack.peek();

                if((c == ')' && top == '(') ||
                   (c == ']' && top == '[') ||
                   (c == '}' && top == '{')) {
                    stack.pop();
                   } else {
                    return false;
                   }
            }
        }

        return stack.isEmpty();
    }
}