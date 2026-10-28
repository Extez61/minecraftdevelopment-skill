package examples
import java.util.UUID
fun main() {
    val gate = SessionGate()
    val a = UUID.randomUUID()
    val b = UUID.randomUUID()
    val old = gate.open(a)
    check(gate.isCurrent(a, old))
    val other = gate.open(b)
    check(gate.isCurrent(a, old) && gate.isCurrent(b, other))
    gate.close(a)
    check(!gate.isCurrent(a, old))
    val newer = gate.open(a)
    check(newer != old && !gate.isCurrent(a, old))
    gate.clear()
    check(!gate.isCurrent(a, newer) && !gate.isCurrent(b, other))
    val newest = gate.open(a)
    check(newest != newer && newest != old && gate.isCurrent(a, newest))
    println("SessionGate Kotlin: PASS")
}
