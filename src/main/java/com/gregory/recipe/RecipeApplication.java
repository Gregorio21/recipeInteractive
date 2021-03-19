package com.gregory.recipe;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;

@SpringBootApplication
public class RecipeApplication {
	//mvnw spring-boot:run         run this command in cmd at project
	public static void main(String[] args) {
		SpringApplication.run(RecipeApplication.class, args);
	}
	
	@GetMapping("/hello")
    public String hello(@RequestParam(value = "name", defaultValue = "World") String name) {
    return String.format("Hello great big %s!", name);
    }
}
