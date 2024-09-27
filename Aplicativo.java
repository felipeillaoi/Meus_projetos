import java.time.LocalTime;
import java.util.Scanner;

public class Aplicativo {
    private Login login;
    private Sensor sensor;

    public Aplicativo() {
        this.login = new Login();
        this.sensor = new Sensor(5.0);
        login.registrar("admin", "1234");
    }

    public void iniciar() {
        System.out.println("Iniciando o aplicativo...");
        Scanner ler = new Scanner(System.in);

        System.out.print("Digite o login: ");
        String loginInput = ler.next();
        System.out.print("Digite a senha: ");
        String senhaInput = ler.next();

        boolean loginValido = login.validar(loginInput, senhaInput);

        if (loginValido) {
            simularLeituraSensor();

            Relatorio relatorio = new Relatorio();
            relatorio.gerarRelatorio(sensor);
        } else {
            System.out.println("Falha no login. Encerrando o aplicativo.");
        }

        ler.close();
    }

    private void simularLeituraSensor() {
        sensor.setHora(LocalTime.now());
        sensor.setEstado(true); // Simula que o sensor está ativo
        sensor.setNivelTurbidezNTU(Math.random() * 10); // Simula um nível de turbidez aleatório
        System.out.println("Dados do sensor recebidos e processados.");
    }
}
