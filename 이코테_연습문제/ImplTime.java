import java.util.*;

public class ImplTime {
    public static void main (String[] args) {
        int n = 5;
        int count = 0;

        for (int hr = 0; hr <= n; hr ++) {
            String strHr = hr + "";
            if (strHr.contains("3")) {
                count += (60*60);
                continue;
            }
            for (int min = 0; min < 60; min ++) {
                String strMin = min + "";
                if (strMin.contains("3")) {
                    count += 60;
                    continue;
                }
                for (int sec = 0; sec < 60; sec ++) {
                    String strSec = sec + "";
                    if (strSec.contains("3")) {
                        count += 1;
                    }
                }
            }
        }
        System.out.println(count);
    }
}
