import java.time.LocalTime;

public class Sensor {
    private LocalTime hora;
    private boolean estado;
    private double nivelTurbidezNTU;
    private double nivelMaximoTurbidez;

    public Sensor(double nivelMaximoTurbidez) {
        this.nivelMaximoTurbidez = nivelMaximoTurbidez;
    }

    public LocalTime getHora() {
        return hora;
    }

    public void setHora(LocalTime hora) {
        this.hora = hora;
    }

    public boolean isEstado() {
        return estado;
    }

    public void setEstado(boolean estado) {
        this.estado = estado;
    }

    public double getNivelTurbidezNTU() {
        return nivelTurbidezNTU;
    }

    public void setNivelTurbidezNTU(double nivelTurbidezNTU) {
        this.nivelTurbidezNTU = nivelTurbidezNTU;
        enviarAlertas();
    }

    public void enviarAlertas() {
        if (this.nivelTurbidezNTU > nivelMaximoTurbidez) {
            System.out.println("Alerta: Nível de turbidez excedido! Valor atual: " + nivelTurbidezNTU + " NTU");
        } else {
            System.out.println("Nível de turbidez dentro do permitido: " + nivelTurbidezNTU + " NTU");
        }
    }
}
