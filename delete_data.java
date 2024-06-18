import java.io.BufferedReader;
import java.io.FileReader;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Random;

public class delete_data {
    public static void main(String[] args) {

        String url = "jdbc:postgresql://127.0.0.1:5432/mydb";
        String user = "lzy";
        String password = "zzz-1234-aaa";
        try (Connection conn = DriverManager.getConnection(url, user, password)) {
            conn.setAutoCommit(false); 
            try {
                String deleteSql = "DELETE FROM sc WHERE grade < 60 order by random() LIMIT 200";
                try (PreparedStatement ps = conn.prepareStatement(deleteSql)) {
                    int rowsAffected = ps.executeUpdate(); 
                    System.out.println("删除了" + rowsAffected+"行");
                }
            } catch (Exception e) {
                e.printStackTrace();
            }
            conn.commit(); // 提交事务
        } catch (Exception e) {
            e.printStackTrace();
        }

    }
}
