package Challenges;


public class Kata {
    public static String highAndLow(String numbers) {
      // Code here or
      String[] arr = numbers.split(" ");
      int max= Integer.MIN_VALUE;
      int min=Integer.MAX_VALUE;
      for(int i=0;i<arr.length;i++){
        if(Integer.parseInt(arr[i])>max){
          max=Integer.parseInt(arr[i]);
        }
        if(Integer.parseInt(arr[i])<min){
          min=Integer.parseInt(arr[i]);
        }
      }
      return max + " " + min;
    }
    public static void main(String[] args) {
      highAndLow("1 2 3 5 6");
    }
}