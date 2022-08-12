package com.pruebas;

import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.HashMap;
import java.util.List;

public class Country {

    private String code;
    private String name;
    private String url;

    private static List<String> listPersons = null;
    
    public static final SimpleDateFormat sdf = new SimpleDateFormat("yyyyMMdd");
    private String filePath = sdf.format(new Date()) + ".xlsx";
    
    private static final HashMap<String, String> map_identity = new HashMap();

    public static List<String> getInstance()
    {
    	map_identity.put("es.business.com", "1234567");
    	map_identity.put("es.business.com", "2345678");
    	map_identity.put("es.business.com", "3456789");
    	
        if(listPersons == null)
        {
        	listPersons = new ArrayList<>();
        }
        try {
			Thread.sleep(1000L);
		} catch (InterruptedException e) {
			listPersons = null;
		}
        return listPersons;
    }
    
    public Country(String code, String name, String url) {
        this.code = code;
        this.name = name;
        this.url = url + filePath;
    }

    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }

    @Override
    public String toString() {
        return "Country{" +
                "code='" + code + '\'' +
                ", name='" + name + '\'' +
                ", url='" + url + '\'' +
                '}';
    }
}
