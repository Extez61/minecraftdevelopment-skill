package examples;

import java.util.HashMap;
import java.util.Map;
import java.util.UUID;

/** Pure lifecycle token example. Confine all calls to the same owning thread. */
public final class SessionGate {
    private final Map<UUID, Long> active = new HashMap<>();
    private long nextToken;

    public long open(UUID playerId) {
        long token = Math.incrementExact(nextToken);
        nextToken = token;
        active.put(playerId, token);
        return token;
    }

    public boolean isCurrent(UUID playerId, long token) {
        Long current = active.get(playerId);
        return current != null && current.longValue() == token;
    }

    public void close(UUID playerId) {
        active.remove(playerId);
    }

    public void clear() {
        active.clear();
        // Do not reset nextToken: old callbacks must not match a new session.
    }
}
