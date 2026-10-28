package examples;
import java.util.UUID;
public final class SessionGateJavaTest {
    private static void check(boolean ok) {
        if (!ok) throw new AssertionError("Session token invariant failed");
    }
    public static void main(String[] args) {
        SessionGate gate = new SessionGate();
        UUID a = UUID.randomUUID(), b = UUID.randomUUID();
        long old = gate.open(a);
        check(gate.isCurrent(a, old));
        long other = gate.open(b);
        check(gate.isCurrent(a, old) && gate.isCurrent(b, other));
        gate.close(a);
        check(!gate.isCurrent(a, old));
        long newer = gate.open(a);
        check(newer != old && !gate.isCurrent(a, old));
        gate.clear();
        check(!gate.isCurrent(a, newer) && !gate.isCurrent(b, other));
        long newest = gate.open(a);
        check(newest != newer && newest != old && gate.isCurrent(a, newest));
        System.out.println("SessionGate Java: PASS");
    }
}
