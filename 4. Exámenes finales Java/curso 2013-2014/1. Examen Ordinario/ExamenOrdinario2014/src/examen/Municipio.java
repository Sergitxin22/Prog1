package examen;

public class Municipio {
	private String nombre;
	private Integer codPostal;
	private Integer numHabitantes;
	private Integer numHogares;
	private double consumoTotalAnual;
	
	public Municipio() {
		super();
	}

	public Municipio(String nombre, Integer codPostal, Integer numHabitantes, Integer numHogares, double consumoTotalAnual) {
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
		return "999 hogares han consumido un total de 999 m3, con una media de 999 m3/habitante";
	}
}
