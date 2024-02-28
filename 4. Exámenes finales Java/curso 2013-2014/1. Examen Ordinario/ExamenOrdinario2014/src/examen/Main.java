package examen;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.Iterator;
import java.util.Scanner;

public class Main {
	
	private static Scanner entrada = new Scanner(System.in);
	
	public static void main(String[] args) {
		// Declaración y creación de los arrays que utiliza el programa
		ArrayList<Municipio> vMunicipios = new ArrayList<Municipio>();
		ArrayList<ArrayList<Integer>> vConsumoMes = new ArrayList<>();
		
		// Procesos previos a la gestión del menú
		cargarMunicipios(vMunicipios);
		
		// Gestion del menú
		int opc;
		do{
			menu();
			
			System.out.print("Opción: ");
			opc = entrada.nextInt();
			
			System.out.print("\n");
			
			switch (opc){
				case 1: registrarConsumoProximo(vMunicipios, vConsumoMes); 
						break;
				case 2: estadoDeposito(vMunicipios); 
						break;
				case 3: visualizarEstadisticaMunicipio(vMunicipios, vConsumoMes); 
						break; 
			}
			
		} while (opc != 4);
		
		entrada.close();
		System.out.println(vMunicipios);
	}
	
	private static void cargarMunicipios(ArrayList<Municipio> vMunicipios) {
		System.out.println("Introduce los municipios");
		
		String opc;
		
		do{
			Municipio municipio = new Municipio().crearMunicipio();
			vMunicipios.add(municipio);
			
			System.out.print("¿Añadir más municipios? (s/n): ");
			opc = entrada.next();
		} while (opc.equals("s"));
		
		
		/*vMunicipios.add(new Municipio("Bilbao", 48002, 12000, 230, 12000.34));
		vMunicipios.add(new Municipio("Cordoba", 23002, 21000, 320, 21010.32));
		vMunicipios.add(new Municipio("Sevilla", 41001, 18000, 300, 17890.45));
		vMunicipios.add(new Municipio("Valencia", 46001, 25000, 400, 24890.78));
		vMunicipios.add(new Municipio("Zaragoza", 50001, 16000, 270, 15900.56));*/
		
		
		vMunicipios.sort((municipio1, municipio2) -> municipio1.getCodPostal() - municipio2.getCodPostal());
	}
	
	private static void menu() {
		System.out.println("\n----");
		System.out.println("MENÚ");
		System.out.println("----");
	    System.out.println("1. Registrar consumo proximo");
	    System.out.println("2. Estado del depósito");
	    System.out.println("3. Visualizar estadística de municipio");
	    System.out.println("4. Salir");
	}
	
	private static double aguaDisponible(ArrayList<Municipio> vMunicipios) {
	    double aguaDisponible = 100_000;
	    for (int i = 0; i < vMunicipios.size(); i++) {
	    	Municipio municipioActual = vMunicipios.get(i);
	    	aguaDisponible -= municipioActual.getConsumoTotalAnual();
		}

	    return aguaDisponible;
	}
	
	private static int indiceMunicipio(Integer codPostal, ArrayList<Municipio> vMunicipios) {		
		for (int i = 0; i < vMunicipios.size(); i++) {
	    	Municipio municipioActual = vMunicipios.get(i);
	    	
	    	if (codPostal == municipioActual.getCodPostal()) {
				return i;
			}
		}
		
		return -1;
	}
	
	private static int leerCPValido(ArrayList<Municipio> vMunicipios) {
		int indice;
		
		System.out.print("Código postal del municipio: ");
		int codpostal = entrada.nextInt();
		indice = indiceMunicipio(codpostal, vMunicipios);
		
		while (indice == -1) {
			System.out.println("¡Error, ese municipio no existe!");
			System.out.print("Código postal del municipio: ");
			codpostal = entrada.nextInt();
			indice = indiceMunicipio(codpostal, vMunicipios);
		}
		
		return indice;
	}
	
	private static void registrarConsumoProximo(ArrayList<Municipio> vMunicipios, ArrayList<ArrayList<Integer>> vConsumoMes) {
		int indiceMunicipio = leerCPValido(vMunicipios);
		Municipio municipio = vMunicipios.get(indiceMunicipio);
		int mesConsumo;
		
		do {
			System.out.print("Mes del próximo consumo [1..12]: ");
			mesConsumo = entrada.nextInt();
		} while (mesConsumo < 1 || mesConsumo > 12);
		
		System.out.print("Consumo estimado a realizar (m3): ");
		int consumoEstimado = entrada.nextInt();
		
		double aguaDisponible = aguaDisponible(vMunicipios);
		
		if (aguaDisponible > consumoEstimado) {
			// En la dimension 1 meto el codPostal, en la 2 el mes y en la 3 el consumoEstimado
			ArrayList<Integer> consumo = new ArrayList<>();
			
            consumo.add(municipio.getCodPostal());
            consumo.add(mesConsumo);
            consumo.add(consumoEstimado);
            
            vConsumoMes.add(consumo);
            
            double consumoMunicipioAnterior = vMunicipios.get(indiceMunicipio).getConsumoTotalAnual();
            vMunicipios.get(indiceMunicipio).setConsumoTotalAnual(consumoEstimado + consumoMunicipioAnterior);
		} else {
			System.out.println("No hay suficiente agua.");
		}
	}
	
	private static void estadoDeposito(ArrayList<Municipio> vMunicipios) {
		double consumoTotal = 100_000 - aguaDisponible(vMunicipios);
		System.out.println("El consumo total realizado es de " + consumoTotal + " m3");
		
		ArrayList<Municipio> vMunicipiosPorConsumo = (ArrayList<Municipio>) vMunicipios.clone();
		vMunicipiosPorConsumo.sort(
				Comparator
		        	.comparingDouble(Municipio::getConsumoTotalAnual)
		        	.reversed()
		);
		
		Municipio municipioMasConsumo = vMunicipiosPorConsumo.get(0);
		System.out.println("El municipio de mayor consumo por habitante es: " + municipioMasConsumo.getNombre());
		
		System.out.println(municipioMasConsumo.crearMensaje());
	}
	


	private static void visualizarEstadisticaMunicipio(ArrayList<Municipio> vMunicipios, ArrayList<ArrayList<Integer>> vConsumoMes) {
		int indiceMunicipio = leerCPValido(vMunicipios);
		Municipio municipio = vMunicipios.get(indiceMunicipio);
		
		System.out.println("El municipio de " + municipio.getNombre() + " ha tenido un consumo total de " + municipio.getConsumoTotalAnual() + " m3");
		System.out.println("Consumo mensual (- representan 100 m3)");
		
		for (int i = 1; i < 13; i++) {
			System.out.print(i + ":");
			int consumoMes = 0;
			
			for (int j = 0; j < vConsumoMes.size(); j++) {
				ArrayList<Integer> consumoActual = vConsumoMes.get(j);
				
				if (consumoActual.get(0) == municipio.getCodPostal() && consumoActual.get(1) == i) {
					consumoMes += consumoActual.get(2);
				}
				
				int numBarras = consumoMes / 100;
				String barras = "";
				
				for (int k = 0; k < numBarras; k++) {
					barras += " -";
				}
				
				System.out.print(barras + "\n");
			}
		}
		
	}

}
