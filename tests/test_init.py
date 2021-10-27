def test_version(db_engine):
    result = db_engine.execute("select version();")
    assert result.fetchone()[0] == "10.5.12-MariaDB-1:10.5.12+maria~focal"