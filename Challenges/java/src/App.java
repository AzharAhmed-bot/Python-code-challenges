package Challenges.java.src;
public class App {
    public static String moveTen(String s){
        StringBuilder result= new StringBuilder();
        for(char c:s.toCharArray()){
            if(Character.isLetter(c)){
                char base=Character.isUpperCase(c)?'A':'a';
                // System.out.println(base);
                char nextTenChar=(char)(((c-base+10)%26)+base);
                result.append(nextTenChar);
            }
            else{
                result.append(c);
            }
        }
        return result.toString();
    }


    public static void main(String[] args) throws Exception {
        System.out.println(moveTen("hello"));
    }
}
