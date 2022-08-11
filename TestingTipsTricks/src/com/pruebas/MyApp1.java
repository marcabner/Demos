package com.pruebas;

import java.text.SimpleDateFormat;
import java.util.Date;

public class MyApp1 {

	public static void main(String[] args) {
		try {
			String fecini = "31/MAR/2020";
			Date pFecIni = new SimpleDateFormat("dd/MMM/yyyy").parse(fecini);
			System.out.println(pFecIni);
			Long N_CHILD = (long) 1.6;
			System.out.println(N_CHILD);
		} catch (Exception e) {
			System.out.println(e.getMessage());
		}

	}

}
