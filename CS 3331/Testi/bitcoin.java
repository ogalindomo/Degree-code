import java.net.*;
import java.util.*;
import java.io.*;
import com.google.appengine.repackaged.org.json.JSONArray;
public class bitcoin
{
    public static void main(String[]args)
    {
        try{
        URL url = new URL("http://www.cs.utep.edu/");
        URLConnection conn = url.openConnection();
        HttpURLConnection httpConn = (HttpURLConnection) conn;
        httpConn.setAllowUserInteraction(false);
        httpConn.setInstanceFollowRedirects(true);
        httpConn.setRequestMethod("GET");
        httpConn.connect();
        if (HttpURLConnection.HTTP_OK == httpConn.getResponseCode()) {
             BufferedReader in = new BufferedReader(new InputStreamReader(httpConn.getInputStream()));
             String str = null;
             
             while((str = in.readLine()) != null)
             {
               System.out.println(str);
             }
        }
      }
      catch(IOException e){}
        
    }
}
