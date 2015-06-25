import org.springframework.boot.*;
import org.springframework.boot.autoconfigure.*;
import org.springframework.stereotype.*;
import org.springframework.web.bind.annotation.*;

@EnableAutoConfiguration
public class ConfigApplication {

    public static void main(String[] args) throws Exception {
        SpringApplication.run(ConfigApplication.class, args);
    }

}
