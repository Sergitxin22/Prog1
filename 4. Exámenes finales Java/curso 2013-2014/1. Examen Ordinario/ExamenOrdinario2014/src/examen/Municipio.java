package examen;

import java.util.Scanner;

public class Municipio {
	private String nombre;
	private int codPostal;
	private int numHabitantes;
	private int numHogares;
	private double consumoTotalAnual;
	
	public Municipio() {
		super();
	}

	public Municipio(String nombre, int codPostal, int numHabitantes, int numHogares, double consumoTotalAnual) {
		super();
		this.nombre = nombre;
		this.codPostal = codPostal;
		this.numHabitantes = numHabitantes;
		this.numHogares = numHogares;
		this.consumoTotalAnual = consumoTotalAnual;
	}

	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public int getCodPostal() {
		return codPostal;
	}

	public void setCodPostal(int codPostal) {
		this.codPostal = codPostal;
	}

	public int getNumHabitantes() {
		return numHabitantes;
	}

	public void setNumHabitantes(int numHabitantes) {
		this.numHabitantes = numHabitantes;
	}

	public int getNumHogares() {
		return numHogares;
	}

	public void setNumHogares(int numHogares) {
		this.numHogares = numHogares;
	}

	public double getConsumoTotalAnual() {
		return consumoTotalAnual;
	}

	public void setConsumoTotalAnual(double consumoTotalAnual) {
		this.consumoTotalAnual = consumoTotalAnual;
	}

	// Métodos  para  leer  de teclado  todos los  atributos  de la  clase,  salvo el consumo anual que se inicializa a cero.
	public Municipio crearMunicipio() {
		Scanner entrada = new Scanner(System.in);
		
		System.out.print("Nombre: ");
		String nombre = entrada.next();
		this.setNombre(nombre);
		
		System.out.print("Código postal: ");
		int codPostal = entrada.nextInt();
		this.setCodPostal(codPostal);
		
		System.out.print("Número de habitantes: ");
		int numHabitantes = entrada.nextInt();
		this.setNumHabitantes(numHabitantes);
		
		System.out.print("Número de hogares: ");
		int numHogares = entrada.nextInt();
		this.setNumHogares(numHogares);
		return this;
	}
	
	@Override
	public String toString() {
		return "Municipio [nombre=" + nombre + ", codPostal=" + codPostal + ", numHabitantes=" + numHabitantes
				+ ", numHogares=" + numHogares + ", consumoTotalAnual=" + consumoTotalAnual + "]";
	}
	
	// Métodos personalizados
	public double consumoMedioHab() {
		return this.consumoTotalAnual / this.numHabitantes;
	}
	
	public String crearMensaje() {
		return "Sus " + this.getNumHogares() + " hogares han consumido un total de " + this.getConsumoTotalAnual() +" m3, con una media de " + this.consumoMedioHab() + " m3/habitante";
	}
}
