package examples

import java.util.UUID

/** Pure lifecycle token example. Confine all calls to the same owning thread. */
class SessionGate {
    private val active = mutableMapOf<UUID, Long>()
    private var nextToken = 0L

    fun open(playerId: UUID): Long {
        val token = Math.incrementExact(nextToken)
        nextToken = token
        active[playerId] = token
        return token
    }

    fun isCurrent(playerId: UUID, token: Long): Boolean = active[playerId] == token

    fun close(playerId: UUID) {
        active.remove(playerId)
    }

    fun clear() {
        active.clear()
        // Do not reset nextToken: old callbacks must not match a new session.
    }
}
