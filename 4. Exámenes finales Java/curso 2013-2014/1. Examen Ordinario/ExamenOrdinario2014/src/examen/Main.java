package examen;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.Scanner;

public class Main {
	private static ArrayList<Municipio> vMunicipios = new ArrayList<Municipio>();
	private static ArrayList<ArrayList<Double>> vConsumoMes = new ArrayList<>();
	
	private static Scanner entrada = new Scanner(System.in);
	
	public static void main(String[] args) {
		
		// Procesos previos a la gestión del menú
		cargarMunicipios();
		System.out.println(vMunicipios);
		
		// Gestion del menú
		int opc;
		do{
			menu();
			
			System.out.print("Opción: ");
			opc = entrada.nextInt();
			
			switch (opc){
				case 1: registrarConsumoProximo(); 
						break;
				case 2: estadoDeposito(); 
						break;
				case 3: visualizarEstadisticaMunicipio(); 
						break; 
			}
			
		} while (opc != 4);
		
		entrada.close();
		System.out.println(vMunicipios);
	}

	private static void cargarMunicipios() {
		vMunicipios.add(new Municipio("Bilbao", 48002, 12000, 230, 12000.34));
		vMunicipios.add(new Municipio("Cordoba", 23002, 21000, 320, 21010.32));
		vMunicipios.add(new Municipio("Sevilla", 41001, 18000, 300, 17890.45));
		vMunicipios.add(new Municipio("Valencia", 46001, 25000, 400, 24890.78));
		vMunicipios.add(new Municipio("Zaragoza", 50001, 16000, 270, 15900.56));
		vMunicipios.sort((municipio1, municipio2) -> municipio1.getCodPostal() - municipio2.getCodPostal());
	}
	
	private static void menu() {
	    System.out.println("1. Registrar consumo proximo");
	    System.out.println("2. Estado del depósito");
	    System.out.println("3. Visualizar estadística de municipio");
	    System.out.println("4. Salir");
	}
	
	private static double aguaDisponible() {
	    double aguaDisponible = 100_000;
	    for (int i = 0; i < vMunicipios.size(); i++) {
	    	Municipio municipioActual = vMunicipios.get(i);
	    	aguaDisponible -= municipioActual.getConsumoTotalAnual();
		}

	    return aguaDisponible;
	}
	
	private static int indiceMunicipio(Integer codPostal) {		
		for (int i = 0; i < vMunicipios.size(); i++) {
	    	Municipio municipioActual = vMunicipios.get(i);
	    	if (codPostal.equals(municipioActual.getCodPostal())) {
				return i;
			}
		}
		
		return -1;
	}
	
	private static int leerCPValido() {
		int indice;
		
		System.out.print("Código postal del municipio: ");
		int codpostal = entrada.nextInt();
		indice = indiceMunicipio(codpostal);
		
		while (indice == -1) {
			System.out.println("¡Error, ese municipio no existe!");
			System.out.print("Código postal del municipio: ");
			codpostal = entrada.nextInt();
			indice = indiceMunicipio(codpostal);
		}
		
		return indice;
	}
	
	private static void registrarConsumoProximo() {
		int indiceMunicipio = leerCPValido();
		
		System.out.println("Mes del próximo consumo [1..12]: ");
		int mesConsumo = entrada.nextInt();
		
		while (mesConsumo < 1 || mesConsumo > 12) {
			System.out.print("Mes del próximo consumo [1..12]: ");
			mesConsumo = entrada.nextInt();
		}
		
		System.out.print("Consumo estimado a realizar (m3): ");
		double consumoEstimado = entrada.nextDouble();
		
		double aguaDisponible = aguaDisponible();
		System.out.println(consumoEstimado);
		System.out.println(aguaDisponible);
		
		if (aguaDisponible > consumoEstimado) {
			// En la dimension uno meto el consumoEstimado y en la 2 el mesConsumo
			ArrayList<Double> consumo = new ArrayList<>();
            consumo.add(consumoEstimado);
            consumo.add((double) mesConsumo);
            vConsumoMes.add(consumo);
            
            double consumoMunicipioAnterior = vMunicipios.get(indiceMunicipio).getConsumoTotalAnual();
            vMunicipios.get(indiceMunicipio).setConsumoTotalAnual(consumoEstimado + consumoMunicipioAnterior);
		} else {
			System.out.println("No hay suficiente agua.");
		}
	}
	
	private static void estadoDeposito() {
		double consumoTotal = 100_000 - aguaDisponible();
		System.out.println("El consumo total realizado es de " + consumoTotal + " m3");
		
		ArrayList<Municipio> vMunicipiosPorConsumo = (ArrayList<Municipio>) vMunicipios.clone();
		vMunicipiosPorConsumo.sort(
				Comparator
		        	.comparingDouble(Municipio::getConsumoTotalAnual)
		        	.reversed()
		);
		
		Municipio municipioMasConsumo = vMunicipiosPorConsumo.get(0);
		System.out.println("El municipio de mayor consumo por habitante es: " + municipioMasConsumo.getNombre());
		

		System.out.println(
				"Sus " + municipioMasConsumo.getNumHogares() + " hogares han consumido un total de " 
				+ municipioMasConsumo.getConsumoTotalAnual() + " m3"
		);
		
		System.out.println("con una media de " + municipioMasConsumo.consumoMedioHab() + " m3/habitante");
	}
	


	private static void visualizarEstadisticaMunicipio() {
		int indiceMunicipio = leerCPValido();
		
		for (int i = 0; i < vConsumoMes.size(); i++) {
			System.out.println(vConsumoMes.get(i));
		}
		
	}

}
