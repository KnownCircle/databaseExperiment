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

public class insert_data {

    public static void main(String[] args) {
        String studentFile = "/home/lzy/data/students5.txt";
        String courseFile = "/home/lzy/data/course3.txt";
        String scFile = "/home/lzy/data/sc2.txt";

        String url = "jdbc:postgresql://127.0.0.1:5432/mydb";
        String user = "lzy";
        String password = "zzz-1234-aaa";

        try (Connection conn = DriverManager.getConnection(url, user, password)) {
            conn.setAutoCommit(false);

            List<String[]> students = read_file(studentFile);
            insert_stu(conn, students);

            List<String[]> course = read_file(courseFile);
            insert_course(conn, course);

            List<String[]> sc = read_file(scFile);
            insert_sc(conn, sc);

            conn.commit(); // 提交事务
            System.out.println("成功插入数据！");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static List<String[]> read_file(String filename) {
        List<String[]> data = new ArrayList<>();
        try (BufferedReader reader = new BufferedReader(new FileReader(filename))) {
            String line;
            while ((line = reader.readLine()) != null && !line.isEmpty()) {
                String[] parts = line.split("\\$");
                data.add(parts);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        return data;
    }

    private static void insert_stu(Connection conn, List<String[]> data) {
        String sql = "INSERT INTO students(sno, sname, sex, bdate, height, dorm) VALUES (?, ?, ?, ?, ?, ?)";
        try (PreparedStatement ps = conn.prepareStatement(sql)) {
            for (String[] row : data) {
                ps.setString(1, row[0]);
                ps.setString(2, row[1]);
                ps.setString(3, row[2]);
                ps.setString(4, row[3]);
                ps.setString(5, row[4]);
                ps.setString(6, row[5]);
                ps.addBatch();
            }
            ps.executeBatch();
        } catch (Exception e) {
            e.printStackTrace();
            try {
                conn.rollback();
            } catch (Exception rollbackException) {
                rollbackException.printStackTrace();
            }
        }
    }

    private static void insert_course(Connection conn, List<String[]> data) {
        String sql = "INSERT INTO course(cno, cname, period, credit, teacher) VALUES (?, ?, ?, ?, ?)";
        try (PreparedStatement ps = conn.prepareStatement(sql)) {
            for (String[] row : data) {
                ps.setString(1, row[0]);
                ps.setString(2, row[1]);
                ps.setString(3, row[2]);
                ps.setString(4, row[3]);
                ps.setString(5, row[4]);
                ps.addBatch();
            }
            ps.executeBatch();
        } catch (Exception e) {
            e.printStackTrace();
            try {
                conn.rollback();
            } catch (Exception rollbackException) {
                rollbackException.printStackTrace();
            }
        }
    }

    private static void insert_sc(Connection conn, List<String[]> data) {
        String sql = "INSERT INTO sc(sno, cno, grade) VALUES (?, ?, ?)";
        try (PreparedStatement ps = conn.prepareStatement(sql)) {
            for (String[] row : data) {
                ps.setString(1, row[0]);
                ps.setString(2, row[1]);
                ps.setString(3, row[2]);
                ps.addBatch();
            }
            ps.executeBatch();
        } catch (Exception e) {
            e.printStackTrace();
            try {
                conn.rollback();
            } catch (Exception rollbackException) {
                rollbackException.printStackTrace();
            }
        }
    }
}
